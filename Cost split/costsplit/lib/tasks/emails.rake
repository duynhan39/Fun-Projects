namespace :emails do
  task mail_activity_reminder: :environment do
    MailActivityReminderJob.perform_later
  end
end
