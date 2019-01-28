class CreateTextstrings < ActiveRecord::Migration[5.2]
  def change
    create_table :textstrings do |t|
      t.string :textstring

      t.timestamps
    end
  end
end
