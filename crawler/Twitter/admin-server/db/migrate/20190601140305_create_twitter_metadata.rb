class CreateTwitterMetadata < ActiveRecord::Migration[5.2]
  def change
    create_table :twitter_metadata do |t|
      t.integer :item_id, limit: 8
      t.string :user_data_name
      t.string :user_screen_name
      t.integer :user_id, limit: 8
      t.integer :sns_id

      t.timestamps
    end
  end
end
