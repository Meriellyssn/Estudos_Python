CREATE VIEW vw_cards_detalhada AS
SELECT 
    c.id,
    c.hp,
    c.name,
    c.info,
    c.attack,
    c.damage,
    c.weak,
    c.resis,
    c.retreat,
    c.cardNumberInCollection,

    -- Substituindo FK por nomes
    col.collectionSetName AS collection_name,
    col.releaseDate,
    col.totalCardsInCollection,

    t.typeName AS type_name,
    s.stageName AS stage_name

FROM tbl_cards c
JOIN tbl_collections col ON c.collection_id = col.id
JOIN tbl_types t ON c.type_id = t.id
JOIN tbl_stages s ON c.stage_id = s.id;