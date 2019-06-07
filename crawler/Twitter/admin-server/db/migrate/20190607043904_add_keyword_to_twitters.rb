class AddKeywordToTwitters < ActiveRecord::Migration[5.2]
  def change
    add_reference :twitters, :keyword, foreign_key: true
  end
end
