CREATE SCHEMA layers;
#DROP TABLE IF EXISTS layers.first_evaluation_indicators;
CREATE TABLE layers.first_evaluation_indicators(id NVARCHAR(5), first_evaluation_indicators VARCHAR(50));
INSERT INTO layers.first_evaluation_indicators
VALUES ('U1','Safety Protection Devices'),
('U2','Main Components'),
('U3','Metal Structure'),
('U4','Electrical Control System'),
('U5','Human Factors'),
('U6','Management and Usage'),
('U7','Environment Factor');