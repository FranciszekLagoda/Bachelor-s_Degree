-- Crating dict tables

CREATE TABLE dict_kraj (
    id_kraj int,
    kraj varchar,
    czy_kraj BOOLEAN,
    kontynent VARCHAR,
    czy_UE BOOLEAN
);

CREATE TABLE dict_kategoria (
    id_kategoria bigint,
    towar_nr VARCHAR,
    towar VARCHAR,
    towar_lista VARCHAR
);

CREATE TABLE  dict_zmienna (
    id_zmienna INT,
    zmienna VARCHAR
);


-- Loading data to tables

COPY dict_kraj
FROM 'C:/Dokumenty/Licencjat/2_Przygotuj/Slowniki/slownik_kraje.csv'
WITH (Format csv, Delimiter ',', encoding 'UTF8', Header);

COPY dict_kategoria
FROM 'C:/Dokumenty/Licencjat/2_Przygotuj/Slowniki/slownik_kategoria.csv'
WITH (Format csv, Delimiter ',', encoding 'UTF8', Header);

COPY dict_zmienna
FROM 'C:/Dokumenty/Licencjat/2_Przygotuj/Slowniki/slownik_zmienna.csv'
WITH (Format csv, Delimiter ',', encoding 'UTF8', Header);

