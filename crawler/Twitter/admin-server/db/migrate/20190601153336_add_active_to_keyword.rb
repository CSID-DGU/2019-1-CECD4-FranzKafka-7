class AddActiveToKeyword < ActiveRecord::Migration[5.2]
  def change
    add_column :keywords, :active, :boolean, default: false
  end
end
