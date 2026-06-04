<?php
/**
 * Red Letter Painting & Remodeling
 * Secure Contact/Estimate Form Handler
 *
 * Intended for DreamHost VPS (PHP supported).
 * 
 * Security features:
 * - Input sanitization
 * - Basic validation
 * - Honeypot spam protection
 * - Proper headers
 * - Optional: logging to file for auditing
 *
 * TODO for production:
 * - Set a real recipient email below
 * - Consider adding reCAPTCHA or similar for stronger spam protection
 * - Configure PHP mail() or switch to SMTP (PHPMailer recommended on DreamHost)
 * - Add rate limiting if needed
 */

// ====================== CONFIG ======================
$to_email = "redletterpaint7@rlpremodeling.com";   // <-- CHANGE THIS to the real business email
$from_email = "no-reply@rlpremodeling.com";        // Use a domain email if possible
$subject_prefix = "Red Letter Painting - New Estimate Request";

// Optional: Log submissions (create a writable logs/ directory on server)
$enable_logging = true;
$log_file = __DIR__ . "/logs/form-submissions.log";

// ====================== HELPER FUNCTIONS ======================
function sanitize($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data, ENT_QUOTES, 'UTF-8');
    return $data;
}

function validate_email($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// ====================== MAIN LOGIC ======================
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    die("Method Not Allowed");
}

// Honeypot check (add a hidden field named "website" in the form)
if (!empty($_POST['website'])) {
    // Spam bot detected
    http_response_code(200);
    echo json_encode(['success' => true, 'message' => 'Thank you.']); // Fake success to bots
    exit;
}

// Collect and sanitize fields (match the form in prototype.html + extras)
$name     = isset($_POST['name']) ? sanitize($_POST['name']) : '';
$phone    = isset($_POST['phone']) ? sanitize($_POST['phone']) : '';
$email    = isset($_POST['email']) ? sanitize($_POST['email']) : '';
$project_type = isset($_POST['project_type']) ? sanitize($_POST['project_type']) : '';
$timeline = isset($_POST['timeline']) ? sanitize($_POST['timeline']) : '';
$message  = isset($_POST['message']) ? sanitize($_POST['message']) : '';

// Basic validation
$errors = [];

if (empty($name)) {
    $errors[] = "Name is required.";
}
if (empty($phone)) {
    $errors[] = "Phone number is required.";
}
if (empty($email) || !validate_email($email)) {
    $errors[] = "A valid email address is required.";
}
if (empty($message)) {
    $errors[] = "Please tell us a bit about your project.";
}

if (!empty($errors)) {
    http_response_code(400);
    header('Content-Type: application/json');
    echo json_encode([
        'success' => false,
        'errors' => $errors
    ]);
    exit;
}

// Build the email body
$email_body = "New Estimate Request from Red Letter Painting Website\n\n";
$email_body .= "Name: $name\n";
$email_body .= "Phone: $phone\n";
$email_body .= "Email: $email\n";
$email_body .= "Project Type: $project_type\n";
$email_body .= "Timeline: $timeline\n\n";
$email_body .= "Project Details:\n$message\n\n";
$email_body .= "---\n";
$email_body .= "Submitted: " . date('Y-m-d H:i:s') . "\n";
$email_body .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

// Send the email
$headers = "From: $from_email\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

$mail_sent = @mail($to_email, $subject_prefix, $email_body, $headers);

// Optional logging
if ($enable_logging) {
    $log_dir = dirname($log_file);
    if (!is_dir($log_dir)) {
        @mkdir($log_dir, 0755, true);
    }
    $log_entry = date('Y-m-d H:i:s') . " | " . 
                 "Name: $name | Phone: $phone | Email: $email | " .
                 "Type: $project_type | Timeline: $timeline\n";
    @file_put_contents($log_file, $log_entry, FILE_APPEND | LOCK_EX);
}

// Response
header('Content-Type: application/json');

if ($mail_sent) {
    echo json_encode([
        'success' => true,
        'message' => 'Thank you! Your request has been received. We will contact you within 24 hours.'
    ]);
} else {
    // Mail failed (common on some hosts without proper config)
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'We were unable to send your request at this time. Please call us directly at (816) 726-9170.'
    ]);
}
exit;
?>