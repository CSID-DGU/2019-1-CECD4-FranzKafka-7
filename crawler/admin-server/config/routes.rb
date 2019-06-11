Rails.application.routes.draw do
  devise_for :admin_users, ActiveAdmin::Devise.config
  ActiveAdmin.routes(self)
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root "admin/dashboard#index"

  get 'twitters/months'=> 'twitters#months'
  get 'twitters/cache_months'=> 'twitters#cache_months'
  get 'dcinsides/months'=> 'dcinsides#months'
  get 'dcinsides/cache_months'=> 'dcinsides#cache_months'
end
