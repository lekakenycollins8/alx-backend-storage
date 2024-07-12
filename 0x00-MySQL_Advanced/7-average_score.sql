-- creates a stored procedure that computes and stores average score for student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    SELECT AVG(score) AS avg_score FROM corrections WHERE user_id = users.id;
    INSERT INTO users (average_score) VALUES (avg_score) WHERE id = user_id;
END $$
DELIMITER ;