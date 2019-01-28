class CreateFmornings < ActiveRecord::Migration[5.2]
  def change
    create_table :fmornings do |t|
      t.string :stdName
      t.integer :urineCol
      t.float :sleepTime
      t.integer :bodySoreness
      t.datetime :subDatetime

      t.timestamps
    end
  end
end
