const prisma = require("../db");

exports.createCategory = async (req, res) => {
  const { c_name } = req.body;
  const c_image = req.file ? req.file.filename : null; // multer-аар авсан зураг

  try {
    const category = await prisma.category.create({
      data: {
        c_name,
        c_image,
      },
    });

    res.status(201).json({
      message: "Амжилттай бүртгэгдлээ",
      category,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      message: "Алдаа гарлаа",
      error: error.message,
    });
  }
};
