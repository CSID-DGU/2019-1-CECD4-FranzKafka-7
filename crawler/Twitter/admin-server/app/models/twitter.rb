class Twitter < ApplicationRecord
    belongs_to :keyword
    validates_uniqueness_of :item_id
    require 'activerecord-import/active_record/adapters/mysql2_adapter'
    def self.json_insert(file, keyword_id)
        p 'start insert'
        
        old_logger = ActiveRecord::Base.logger
        ActiveRecord::Base.logger = nil
        
        json = JSON.parse(file)
        size = json.size
        tweets = []

        json.each_with_index do |j,i|
            
            j.delete("html")
            j.delete("url")
            p_date = DateTime.parse(j.delete("timestamp"))
            j["item_id"] = j.delete("id")
            j["content"] = j.delete("text")
            j["name"] = j.delete("user")
            j["keyword_id"] = keyword_id
            j["p_date"] = p_date
            tweets << Twitter.new(j)
            
            if i%1000 == 0 or i == size-1
                begin
                    Twitter.import tweets, validate_uniqueness: true
                    tweets = []
                rescue Exception => e
                    p e.message
                    next
                end
            end
            
        end
        ActiveRecord::Base.logger = old_logger
    end
end
