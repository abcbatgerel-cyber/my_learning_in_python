const express = require("express");
const router = express.Router();
const { createCategory } = require("../controller/categoryController");
const upload = require("../middleware/multer");

router.post("/create", upload.single("file"), createCategory);

module.exports = router;
