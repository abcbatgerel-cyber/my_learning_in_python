const express = require("express");
const app = express();
const userRouter = require("./router/user_router");
const categoryRouter = require("./router/categoryRouter");

app.use(express.json()); 
app.use(express.urlencoded({ extended: true }));

app.use("/users", userRouter);
app.use("/category", categoryRouter);

app.listen(3000, () => {
  console.log("Server listen 3000 port");
});
