class ActivityMailer < ActionMailer::Base
  default from: "troyforms@gmail.com"

  def factivity_required(email)
    mail(to: email, subject: 'Activity Form Required')
  end
  def fmorning_required(email)
    mail(to: email, subject: 'Morning Form Required')
  end
end
