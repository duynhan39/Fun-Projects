class SendActivityReminderJob < ApplicationJob
  queue_as :default

  def perform(athletes)
      ActivityMailer.factivity_required("esgameday.2@gmail.com").deliver_later
  end
end
