class CreateTwitterMetadata < ActiveRecord::Migration[5.2]
  def change
    create_table :twitter_metadata do |t|
      t.integer :item_id
      t.string :user_data_name
      t.string :user_screen_name
      t.integer :user_id
      t.references :sns, foreign_key: true

      t.timestamps
    end
  end
end
