class CreateSns < ActiveRecord::Migration[5.2]
  def change
    create_table :sns do |t|
      t.datetime :p_date
      t.text :content
      t.references :keyword, foreign_key: true

      t.timestamps
    end
  end
end
