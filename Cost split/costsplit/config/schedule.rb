# Learn more: http://github.com/javan/whenever

env :PATH, ENV['PATH']

every 1.days, at: '10:55 am' do
  runner "Athlete.fmorning_email", :environment => 'development'
end
every 1.days, at: ['9:00 am', '6:15 pm'] do
  runner "Athlete.factivity_email", :environment => 'development'
end
