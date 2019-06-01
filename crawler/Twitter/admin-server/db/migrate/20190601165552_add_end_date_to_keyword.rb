class AddEndDateToKeyword < ActiveRecord::Migration[5.2]
  def change
    add_column :keywords, :end_date, :datetime, default: -> { 20100101000000 }
  end
end
