class ConvertCharsettoUtf8mb4 < ActiveRecord::Migration[5.2]
  def change
    execute("ALTER TABLE sns CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    #execute("ALTER TABLE sns CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;")
    #execute("ALTER TABLE sns MODIFY content VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin, MODIFY user_data_name VARCHAR(255) SET utf8mb4 COLLATE utf8mb4_bin, MODIFY user_screen_name VARCHAR(255) SET utf8mb4 COLLATE utf8mb4_bin;")
    
    # config = Rails.configuration.database_configuration
    # db_name = config[Rails.env]["database"]
    # collate = 'utf8mb4_polish_ci'
    # char_set = 'utf8mb4'
    # row_format = 'DYNAMIC'
 
    # execute("ALTER DATABASE #{db_name} CHARACTER SET #{char_set} COLLATE #{collate};")
 
    # ActiveRecord::Base.connection.tables.each do |table|
    #   execute("ALTER TABLE #{table} ROW_FORMAT=#{row_format};")
    #   execute("ALTER TABLE #{table} CONVERT TO CHARACTER SET #{char_set} COLLATE #{collate};")
    # end
    
  end
end
