class AddScheduleToAthlete < ActiveRecord::Migration[5.2]
  def change
    add_column :athletes, :schedule, :text
  end
end
