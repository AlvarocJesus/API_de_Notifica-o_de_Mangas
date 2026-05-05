CREATE TABLE "site"(
    "id" BIGINT NOT NULL,
    "url" VARCHAR(255) NOT NULL,
    "ativo" BOOLEAN NOT NULL
);
ALTER TABLE "site"
ADD PRIMARY KEY("id");
CREATE TABLE "manga"(
    "id" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "total_cap" SMALLINT NOT NULL DEFAULT '0',
    "temporadas" SMALLINT NOT NULL DEFAULT '0',
    "tipo" CHAR(255) NOT NULL
);
ALTER TABLE "manga"
ADD PRIMARY KEY("id");
COMMENT ON COLUMN "manga"."nome" IS 'Coluna com o nome do anime, manga ou filme';
COMMENT ON COLUMN "manga"."total_cap" IS 'Coluna para o total de capitulos, episodios';
COMMENT ON COLUMN "manga"."temporadas" IS 'Coluna para o total de temporadas';
COMMENT ON COLUMN "manga"."tipo" IS 'Coluna para guardar qual o tipo de midia';
CREATE TABLE "table_4"(
    "id" BIGINT NOT NULL,
    "userId" BIGINT NOT NULL,
    "mangaId" BIGINT NOT NULL
);
ALTER TABLE "table_4"
ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "id" BIGINT NOT NULL,
    "nome" VARCHAR(255) NOT NULL
);
ALTER TABLE "user"
ADD PRIMARY KEY("id");
ALTER TABLE "manga"
ADD CONSTRAINT "manga_id_foreign" FOREIGN KEY("id") REFERENCES "site"("id");
ALTER TABLE "table_4"
ADD CONSTRAINT "table_4_id_foreign" FOREIGN KEY("id") REFERENCES "user"("id");
ALTER TABLE "table_4"
ADD CONSTRAINT "table_4_id_foreign" FOREIGN KEY("id") REFERENCES "manga"("id");