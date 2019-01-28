namespace :ereminder do
  desc "Send activity email"
  task activity_reminder: :environment do
    SendActivityReminderJob.perform_later
  end
end
