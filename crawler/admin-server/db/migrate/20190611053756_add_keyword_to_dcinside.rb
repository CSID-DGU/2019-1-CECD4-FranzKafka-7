class AddKeywordToDcinside < ActiveRecord::Migration[5.2]
  def change
    add_reference :dcinsides, :keyword, foreign_key: true
  end
end
