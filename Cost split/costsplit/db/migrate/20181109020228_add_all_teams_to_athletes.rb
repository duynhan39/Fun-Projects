class AddAllTeamsToAthletes < ActiveRecord::Migration[5.2]
  def change
    add_column :athletes, :all_teams, :string
  end
end
