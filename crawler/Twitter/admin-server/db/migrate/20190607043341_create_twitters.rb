class CreateTwitters < ActiveRecord::Migration[5.2]
  def change
    create_table :twitters do |t|
      t.string :fullname
      t.string :name
      t.integer :item_id, limit: 8
      t.integer :likes
      t.integer :replies
      t.integer :retweets
      t.text :content
      t.datetime :p_date

      t.timestamps
    end
  end
end
