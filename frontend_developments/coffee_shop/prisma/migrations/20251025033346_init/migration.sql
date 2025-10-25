-- CreateTable
CREATE TABLE "user" (
    "id" SERIAL NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "password" VARCHAR(100) NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "user_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "UserInfo" (
    "id" SERIAL NOT NULL,
    "username" VARCHAR(45) NOT NULL,
    "first_name" VARCHAR(45),
    "last_name" VARCHAR(45),
    "address" VARCHAR(255) NOT NULL,
    "phone_number" INTEGER NOT NULL,
    "profile" VARCHAR(255),
    "userId" INTEGER NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "UserInfo_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Category" (
    "id" SERIAL NOT NULL,
    "c_name" VARCHAR(25) NOT NULL,
    "c_image" VARCHAR(45) NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Category_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Product" (
    "id" SERIAL NOT NULL,
    "p_title" VARCHAR(255) NOT NULL,
    "p_image" VARCHAR(255) NOT NULL,
    "price" INTEGER NOT NULL,
    "p_desc" TEXT NOT NULL,
    "c_name" TEXT NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "update_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Product_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "UserInfo_username_key" ON "UserInfo"("username");

-- CreateIndex
CREATE UNIQUE INDEX "UserInfo_first_name_key" ON "UserInfo"("first_name");

-- CreateIndex
CREATE UNIQUE INDEX "UserInfo_last_name_key" ON "UserInfo"("last_name");

-- CreateIndex
CREATE UNIQUE INDEX "UserInfo_userId_key" ON "UserInfo"("userId");

-- CreateIndex
CREATE UNIQUE INDEX "Category_c_name_key" ON "Category"("c_name");

-- AddForeignKey
ALTER TABLE "UserInfo" ADD CONSTRAINT "UserInfo_userId_fkey" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Product" ADD CONSTRAINT "Product_c_name_fkey" FOREIGN KEY ("c_name") REFERENCES "Category"("c_name") ON DELETE RESTRICT ON UPDATE CASCADE;