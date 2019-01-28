class CreateFactivities < ActiveRecord::Migration[5.2]
  def change
    drop_table :factivities
    create_table :factivities do |t|
      t.string :stdName
      t.string :activity
      t.integer :exertion

      t.timestamps
    end
  end
end
