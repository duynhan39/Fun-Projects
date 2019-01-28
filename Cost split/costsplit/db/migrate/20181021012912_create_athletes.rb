class CreateAthletes < ActiveRecord::Migration[5.2]
  def change
    create_table :athletes do |t|
      t.string :name
      t.string :email
      t.integer :phone

      t.timestamps
    end
  end
end
