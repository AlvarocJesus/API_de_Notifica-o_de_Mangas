CREATE TABLE "users" (
  "id_user" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "manga_user" (
  "id" int,
  "atual_cap" int,
  "atual_temporada" int,
  "userId" fk,
  "mangaId" fk
);

CREATE TABLE "mangas" (
  "id_manga" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar,
  "total_caps" int,
  "temporadas" int,
  "tipo" fk
);

CREATE TABLE "sites" (
  "id_site" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "url" varchar,
  "ativo" bool,
  "mangaId" fk
);

CREATE TABLE "genero" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "genero" varchar
);

CREATE TABLE "Manga_Genero" (
  "id" INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "id_manga" fk,
  "id_genero" fk
);

ALTER TABLE "sites" ADD FOREIGN KEY ("mangaId") REFERENCES "mangas" ("id_manga");

ALTER TABLE "manga_user" ADD FOREIGN KEY ("userId") REFERENCES "users" ("id_user");

ALTER TABLE "manga_user" ADD FOREIGN KEY ("mangaId") REFERENCES "mangas" ("id_manga");

ALTER TABLE "Manga_Genero" ADD FOREIGN KEY ("id_genero") REFERENCES "genero" ("id");

ALTER TABLE "Manga_Genero" ADD FOREIGN KEY ("id_manga") REFERENCES "mangas" ("tipo");
