BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Barcodes" (
	"Name"	TEXT,
	"Type"	TEXT,
	"Number"	INTEGER,
	"Waste Bin"	TEXT,
	"Instructions"	TEXT
);
INSERT INTO "Barcodes" VALUES ('Coca-Cola, 8 ct, 7.5 FL OZ Mini-Can','soda can',49000052350,'Recycle','Empty excess liquid, rinse out can if possible. Place clean and dry can in nearest recycle bin');
INSERT INTO "Barcodes" VALUES ('Nature Valley Granola Bar, Oats and Honey','food wrapper',16000264694,'Landfill','Excess food may be placed in compost, the wrapper must be thrown in landfill');
INSERT INTO "Barcodes" VALUES ('DairyPure 2% Reduced Fat Milk - 1 Gallon','milk carton',41900076610,'Recycle','Empty and rinse any excess liquid. Dispose of clean and dry container in Recycle bin');
INSERT INTO "Barcodes" VALUES ('Mott''s Medleys Fruit Snacks, Assorted Fruit Gluten Free Snacks, Family Size, 40 Pouches, 0.8 oz Each','food container',16000487642,'Recycle','Dispose of cardboard box in nearest recycle bin. Ensure no leftover food is in the box.');
INSERT INTO "Barcodes" VALUES ('General Mills Multigrain Cheerios Cereal, Lightly Sweetened, 37.5 Ounce','food container',16000401051,'Recycle','Any excess cereal may go into Compost. The plastic bag must go into landfill. The cardboard box can be recycled');
INSERT INTO "Barcodes" VALUES (NULL,'spoon',-1,'Landfill','Dispose in landfill bin');
INSERT INTO "Barcodes" VALUES (NULL,'fork',-1,'Landfill','Dispose in landfill bin');
INSERT INTO "Barcodes" VALUES ('','knife',-1,'Landfill','Dispose in landfill bin');
INSERT INTO "Barcodes" VALUES ('Coke, 20 oz','bottle',49000000443,'Recycle','Empty and rinse excess liquid. Dispose clean and dry bottle in bin.');
INSERT INTO "Barcodes" VALUES ('Lay''s Potato Chips, Party Size Classic, 13.75 Oz','chip bag',28400164733,'Landfill','Excess food may be placed in compost, the wrapper must be thrown in landfill');
COMMIT;
