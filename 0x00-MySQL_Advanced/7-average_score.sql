-- creates a stored procedure that computes and stores average score for student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10,2);
    SELECT AVG(score) INTO avg_score FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET average_score = avg_score WHERE users.id = user_id;
END $$
DELIMITER ;