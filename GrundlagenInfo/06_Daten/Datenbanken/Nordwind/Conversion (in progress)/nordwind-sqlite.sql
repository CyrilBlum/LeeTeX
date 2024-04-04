-- import to SQLite by running: sqlite3.exe db.sqlite3 -init sqlite.sql

PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;
BEGIN TRANSACTION;


CREATE TABLE `Artikel` (
`ArtikelNr` DOUBLE,
`Artikelname` TEXT,
`LieferantenNr` DOUBLE,
`KategorieNr` DOUBLE,
`Liefereinheit` TEXT,
`Einzelpreis` DOUBLE,
`Lagerbestand` DOUBLE,
`BestellteEinheiten` DOUBLE,
`Mindestbestand` DOUBLE,
`Auslaufartikel` DOUBLE
);
INSERT INTO `Artikel` (`ArtikelNr`,`Artikelname`,`LieferantenNr`,`KategorieNr`,`Liefereinheit`,`Einzelpreis`,`Lagerbestand`,`BestellteEinheiten`,`Mindestbestand`,`Auslaufartikel`)
VALUES
(1,'Chai',1,1,'10 Kartons x 20 Beutel',18,39,0,10,1),
(2,'Chang',1,1,'24 x 12-oz-Flaschen',19,17,40,25,1),
(3,'Aniseed Syrup',1,2,'12 x 550-ml-Flaschen',10,13,70,25,0),
(4,'Chef Anton''s Cajun Seasoning',2,2,'48 x 6-oz-Gläser',22,53,0,0,1),
(5,'Chef Anton''s Gumbo Mix',2,2,'36 Kartons',21.35,0,0,0,1),
(6,'Grandma''s Boysenberry Spread',3,2,'12 x 8-oz-Gläser',25,120,0,25,0),
(7,'Uncle Bob''s Organic Dried Pears',3,7,'12 x 1-lb-Packungen',30,15,0,10,1),
(8,'Northwoods Cranberry Sauce',3,2,'12 x 12-oz-Gläser',40,6,0,0,0),
(9,'Mishi Kobe Niku',4,6,'18 x 500-g-Packungen',97,29,0,0,1),
(10,'Ikura',4,8,'12 x 200-ml-Gläser',31,31,0,0,0),
(11,'Queso Cabrales',5,4,'1-kg-Paket',21,22,30,30,0),
(12,'Queso Manchego La Pastora',5,4,'10 x 500-g-Packungen',38,86,0,0,0),
(13,'Konbu',6,8,'2-kg-Karton',6,24,0,5,0),
(14,'Tofu',6,7,'40 x 100-g-Packungen',23.25,35,0,0,0),
(15,'Genen Shouyu',6,2,'24 x 250-ml-Flaschen',15.5,39,0,5,0),
(16,'Pavlova',7,3,'32 x 500-g-Kartons',17.45,29,0,10,0),
(17,'Alice Mutton',7,6,'20 x 1-kg-Dosen',39,0,0,0,1),
(18,'Carnarvon Tigers',7,8,'16-kg-Paket',62.5,42,0,0,0),
(19,'Teatime Chocolate Biscuits',8,3,'10 Kartons x 12 Stück',9.2,25,0,5,0),
(20,'Sir Rodney''s Marmalade',8,3,'30 Geschenkkartons',81,40,0,0,0),
(21,'Sir Rodney''s Scones',8,3,'24 Packungen x 4 Stück',10,3,40,5,0),
(22,'Gustaf''s Knäckebröd',9,5,'24 x 500-g-Packungen',21,104,0,25,0),
(23,'Tunnbröd',9,5,'12 x 250-g-Packungen',9,61,0,25,0),
(24,'Guaraná Fantástica',10,1,'12 x 355-ml-Dosen',4.5,20,0,0,1),
(25,'NuNuCa Nuß-Nougat-Creme',11,3,'20 x 450-g-Gläser',14,76,0,30,0),
(26,'Gumbär Gummibärchen',11,3,'100 x 250-g-Beutel',31.23,15,0,0,1),
(27,'Schoggi Schokolade',11,3,'100 x 100-g-Stück',43.9,49,0,30,0),
(28,'Rössle Sauerkraut',12,7,'25 x 825-g-Dosen',45.6,26,0,0,1),
(29,'Thüringer Rostbratwurst',12,6,'50 Beutel x 30 Würstchen',123.79,0,0,0,1),
(30,'Nord-Ost Matjeshering',13,8,'10 x 200-g-Gläser',25.89,10,0,15,0),
(31,'Gorgonzola Telino',14,4,'12 x 100-g-Packungen',12.5,0,70,20,0),
(32,'Mascarpone Fabioli',14,4,'24 x 200-g-Packungen',32,9,40,25,0),
(33,'Geitost',15,4,'500-g-Packung',2.5,112,0,20,0),
(34,'Sasquatch Ale',16,1,'24 x 12-oz-Flaschen',14,111,0,15,0),
(35,'Steeleye Stout',16,1,'24 x 12-oz-Flaschen',18,20,0,15,0),
(36,'Inlagd Sill',17,8,'24 x 250-g -Gläser',19,112,0,20,0),
(37,'Gravad lax',17,8,'12 x 500-g-Packungen',26,11,50,25,0),
(38,'Côte de Blaye',18,1,'12 x 75-cl-Flaschen',263.5,17,0,15,0),
(39,'Chartreuse verte',18,1,'750-ml-Flasche',18,69,0,5,0),
(40,'Boston Crab Meat',19,8,'24 x 4-oz-Dosen',18.4,123,0,30,0),
(41,'Jack''s New England Clam Chowder',19,8,'12 x 12-oz-Dosen',9.65,85,0,10,0),
(42,'Singaporean Hokkien Fried Mee',20,5,'32 x 1-kg-Packungen',14,26,0,0,1),
(43,'Ipoh Coffee',20,1,'16 x 500-g-Dosen',46,17,10,25,0),
(44,'Gula Malacca',20,2,'20 x 2-kg-Beutel',19.45,27,0,15,0),
(45,'Røgede sild',21,8,'1-kg-Paket',9.5,5,70,15,0),
(46,'Spegesild',21,8,'4 x 450-g-Gläser',12,95,0,0,0),
(47,'Zaanse koeken',22,3,'10 x 4-oz-Kartons',9.5,36,0,0,0),
(48,'Chocolade',22,3,'10 Packungen',12.75,15,70,25,0),
(49,'Maxilaku',23,3,'24 x 50-g-Packungen',20,10,60,15,0),
(50,'Valkoinen suklaa',23,3,'12 x 100-g-Riegel',16.25,65,0,30,0),
(51,'Manjimup Dried Apples',24,7,'50 x 300-g-Packungen',53,20,0,10,0),
(52,'Filo Mix',24,5,'16 x 2-kg-Kartons',7,38,0,25,0),
(53,'Perth Pasties',24,6,'48 Stück',32.8,0,0,0,1),
(54,'Tourtière',25,6,'16 Pasteten',7.45,21,0,10,0),
(55,'Pâté chinois',25,6,'24 Kartons x 2 Pasteten',24,115,0,20,0),
(56,'Gnocchi di nonna Alice',26,5,'24 x 250-g-Packungen',38,21,10,30,0),
(57,'Ravioli Angelo',26,5,'24 x 250-g-Packungen',19.5,36,0,20,0),
(58,'Escargots de Bourgogne',27,8,'24 Stück',13.25,62,0,20,0),
(59,'Raclette Courdavault',28,4,'5-kg-Packung',55,79,0,0,0),
(60,'Camembert Pierrot',28,4,'15 x 300-g-Stücke',34,19,0,0,0),
(61,'Sirop d''érable',29,2,'24 x 500-ml-Flaschen',28.5,113,0,25,0),
(62,'Tarte au sucre',29,3,'48 Törtchen',49.3,17,0,0,0),
(63,'Vegie-spread',7,2,'15 x 625-g-Gläser',43.9,24,0,5,0),
(64,'Wimmers gute Semmelknödel',12,5,'20 Beutel x 4 Stück',33.25,22,80,30,0),
(65,'Louisiana Fiery Hot Pepper Sauce',2,2,'32 x 8-oz-Flaschen',21.05,76,0,0,0),
(66,'Louisiana Hot Spiced Okra',2,2,'24 x 8-oz-Gläser',17,4,100,20,1),
(67,'Laughing Lumberjack Lager',16,1,'24 x 12-oz-Flaschen',14,52,0,10,0),
(68,'Scottish Longbreads',8,3,'10 Kartons x 8 Stück',12.5,6,10,15,0),
(69,'Gudbrandsdalsost',15,4,'10-kg-Paket',36,26,0,15,0),
(70,'Outback Lager',7,1,'24 x 355-ml-Flaschen',15,15,10,30,0),
(71,'Fløtemysost',15,4,'10 x 500-g-Packungen',21.5,26,0,0,0),
(72,'Mozzarella di Giovanni',14,4,'24 x 200 g-Packungen',34.8,14,0,0,0),
(73,'Röd Kaviar',17,8,'24 x 150-g-Gläser',15,101,0,5,0),
(74,'Longlife Tofu',4,7,'5-kg-Paket',10,4,20,5,0),
(75,'Rhönbräu Klosterbier',12,1,'24 x 0,5-l-Flaschen',7.75,125,0,25,0),
(76,'Lakkalikööri',23,1,'500-ml-Flasche',18,57,0,20,0),
(77,'Original Frankfurter grüne Soße',12,2,'12 Kartons',13,32,0,15,0),
(79,'Darmstädter Obstgarten',16,1,'2 kg',2.5,0,0,0,0);

CREATE TABLE `Kategorie` (
`KategorieNr` DOUBLE,
`Kategoriename` TEXT,
`Beschreibung` TEXT
);
INSERT INTO `Kategorie` (`KategorieNr`,`Kategoriename`,`Beschreibung`)
VALUES
(1,'Getränke','Alkoholfreie Getränke, Kaffee, Tee, Bier'),
(2,'Gewürze','Süße und saure Soßen, Gewürze'),
(3,'Süßwaren','Desserts und Süßigkeiten'),
(4,'Milchprodukte','Käsesorten'),
(5,'Getreideprodukte','Brot, Kräcker, Nudeln, Müsli'),
(6,'Fleischprodukte','Fleisch-Fertiggerichte'),
(7,'Naturprodukte','Getrocknete Früchte, Tofu usw.'),
(8,'Meeresfrüchte','Meerespflanzen und -früchte, Fisch');





COMMIT;
PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
