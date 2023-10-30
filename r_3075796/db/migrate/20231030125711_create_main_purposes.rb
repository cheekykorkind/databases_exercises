class CreateMainPurposes < ActiveRecord::Migration[7.1]
  def change
    create_table :main_purposes do |t|
      t.string :purpose

      t.timestamps
    end
  end
end
