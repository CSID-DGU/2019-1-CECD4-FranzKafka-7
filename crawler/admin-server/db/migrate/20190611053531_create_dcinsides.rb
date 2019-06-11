class CreateDcinsides < ActiveRecord::Migration[5.2]
  def change
    create_table :dcinsides do |t|
      t.string :user_id
      t.text :body
      t.integer :view_dn
      t.string :title
      t.integer :post_no
      t.integer :view_up
      t.datetime :written_at
      t.string :gall_id
      t.string :nickname
      t.integer :comment_cnt
      t.integer :view_cnt
      t.string :user_ip

      t.timestamps
    end
  end
end
