# Load the Rails application.
require_relative 'application'

# Load ActionMailer smtp config
# SMTP settings for gmail
Rails.application.configure do
config.action_mailer.smtp_settings = {
  :address              => "smtp.gmail.com",
  :port                 => 587,
  :user_name            => ENV['gmail_username'],
  :password             => ENV['gmail_password'],
  :authentication       => "plain",
  :enable_starttls_auto => true
  }
end

# Initialize the Rails application.
Rails.application.initialize!
