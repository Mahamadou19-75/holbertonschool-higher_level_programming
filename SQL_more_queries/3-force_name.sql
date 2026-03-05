-- Crée la table `force_name` si elle n'existe pas déjà avec les champs spécifiés
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
