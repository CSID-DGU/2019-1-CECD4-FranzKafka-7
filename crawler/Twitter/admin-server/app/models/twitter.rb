class Twitter < ApplicationRecord
    belongs_to :keyword
    validates_uniqueness_of :item_id

    def self.json_insert(file, keyword_id)
        p 'start insert'
        old_logger = ActiveRecord::Base.logger
        ActiveRecord::Base.logger = nil

        json = JSON.parse(file)
        json.each do |j|
            
            j.delete("html")
            j.delete("url")
            p_date = DateTime.parse(j.delete("timestamp"))
            j["item_id"] = j.delete("id")
            j["content"] = j.delete("text")
            j["name"] = j.delete("user")
            j["keyword_id"] = keyword_id
            j["p_date"] = p_date
            t = Twitter.new(j)
            begin
                t.save!
            rescue ActiveRecord::RecordInvalid => e
                next
            end

        ActiveRecord::Base.logger = old_logger


        end
    end
end
