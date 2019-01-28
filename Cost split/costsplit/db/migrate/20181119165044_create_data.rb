class CreateData < ActiveRecord::Migration[5.2]
  def change
    create_table :data do |t|
      t.string :stdName
      t.float :calculation

      t.timestamps
    end
  end
end
