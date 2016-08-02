SELECT 
  username, control, login_count, avg_login_time,
  affirmation_count, AVG_affirmation_len, encouragments_given, encouragements_received
FROM users_user
INNER JOIN (
    SELECT
      user_id, AVG(CAST(EXTRACT(EPOCH FROM (logout_time - time)) AS FLOAT)) avg_login_time
    FROM users_login
    WHERE user_id != 3
    GROUP BY user_id
) logins
ON logins.user_id = users_user.id
INNER JOIN(
    SELECT
        user_id, COUNT(*) affirmation_count, AVG(length(text)) avg_affirmation_len
    FROM users_affirmation
    GROUP BY user_id
) affirmations
ON affirmations.user_id = users_user.id
LEFT OUTER JOIN(
    SELECT encourager_id, COUNT(*) encouragments_given FROM users_encouragement
    GROUP BY encourager_id
) given
ON given.encourager_id = users_user.id
LEFT OUTER JOIN(
    SELECT
        users_affirmation.user_id, COUNT(*) encouragements_received
    FROM users_encouragement
    INNER JOIN users_affirmation
    ON users_affirmation.id = users_encouragement.affirmation_id
    GROUP BY users_affirmation.user_id
) received
ON received.user_id = users_user.id
WHERE
  dummy_user = FALSE AND
  username != 'kazanz';
