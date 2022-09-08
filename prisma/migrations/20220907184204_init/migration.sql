/*
  Warnings:

  - You are about to drop the column `UpdatedAt` on the `Manga` table. All the data in the column will be lost.
  - You are about to drop the column `UpdatedAt` on the `User` table. All the data in the column will be lost.
  - Added the required column `total_chapter` to the `Manga` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Manga" DROP COLUMN "UpdatedAt",
ADD COLUMN     "total_chapter" INTEGER NOT NULL,
ADD COLUMN     "updatedAt" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
ALTER COLUMN "current_chapter" SET DEFAULT 0,
ALTER COLUMN "updated_chapter" SET DEFAULT 0;

-- AlterTable
ALTER TABLE "User" DROP COLUMN "UpdatedAt",
ADD COLUMN     "updatedAt" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP;

-- CreateTable
CREATE TABLE "consulting_sites" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "url" VARCHAR(255) NOT NULL,

    CONSTRAINT "consulting_sites_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "consulting_sites_name_key" ON "consulting_sites"("name");

-- CreateIndex
CREATE UNIQUE INDEX "consulting_sites_url_key" ON "consulting_sites"("url");
