const prisma = require("../db");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

exports.Register = async (req, res) => {
  const { email, password } = req.body;

  try {
    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(password, salt);

    const user = await prisma.user.create({
      data: { email, password: hashPassword },
    });

    res.status(201).json({
      message: "Амжилттай бүртгэгдлээ",
      user,
    });
  } catch (error) {
    res.status(500).json({
      message: "Алдаа гарлаа",
      error: error.message,
    });
  }
};

exports.Login = async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = await prisma.user.findUnique({ where: { email } });

    if (!user)
      return res.status(404).json({ message: "Бүртгэлтэй хэрэглэгч олдсонгүй" });

    const correctPass = await bcrypt.compare(password, user.password);
    if (!correctPass)
      return res.status(404).json({ message: "Нууц үг эсвэл email буруу байна" });

    const token = jwt.sign(
      { mail: user.email, id: user.id },
      process.env.JWT_SECRET,
      { expiresIn: "1h" }
    );

    res.status(200).json({ message: "Амжилттай нэвтэрлээ", token });
  } catch (error) {
    res.status(500).json({
      message: "Алдаа гарлаа",
      error: error.message,
    });
  }
};
