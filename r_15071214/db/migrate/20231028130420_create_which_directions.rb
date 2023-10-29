class CreateWhichDirections < ActiveRecord::Migration[7.1]
  def change
    create_table :which_directions do |t|
      t.string :direction

      t.timestamps
    end
  end
end
