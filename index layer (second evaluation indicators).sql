#DROP TABLE IF EXISTS layers.second_evaluation_indicators;
CREATE TABLE layers.second_evaluation_indicators(id NVARCHAR(5), parent_id NVARCHAR(5),first_evaluation_indicators VARCHAR(50));
INSERT INTO layers.second_evaluation_indicators VALUES 
('U11','U1','Brake'),
('U12','U1','Limiting Devices'),
('U13','U1','Anti-Collision Devices'),
('U14','U1','Buffer And End Stopper'),
('U15','U1','Anti-Wind And Anti-Slip Devices'),
('U16','U1','Interlock Protection Switch'),
('U17','U1','Warning Device'),
('U21','U2','Hook'),
('U22','U2','Wire Rope'),
('U23','U2','Drum'),
('U24','U2','Pulley'),
('U25','U2','Wheel'),
('U26','U2','Reducer'),
('U27','U2','Track'),
('U28','U2','Coupling'),
('U31','U3','Main Beam'),
('U32','U3','Arch Beam/Camber'),
('U33','U3','I Beam'),
('U41','U4','Power Supply Switch'),
('U42','U4','Emergency Stop Switch'),
('U43','U4','Electrical Grounding Systems'),
('U44','U4','Insulation Resistance'),
('U45','U4','Protection Devices'),
('U51','U5','Quality of Regulatory Personnel'),
('U52','U5','Command Personnel Proficiency'),
('U61','U6','Management System'),
('U62','U6','Maintenance Situation'),
('U63','U6','Inspection Situation'),
('U71','U7','Operating Environment'),
('U72','U7','Drivers cab'),
('U73','U7','Working Area');