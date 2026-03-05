-- Crée la base de données `hbtn_0d_2` si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur `user_0d_2` avec un mot de passe, s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorde le privilège SELECT sur la base de données `hbtn_0d_2` à `user_0d_2`
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applique les privilèges
FLUSH PRIVILEGES;
