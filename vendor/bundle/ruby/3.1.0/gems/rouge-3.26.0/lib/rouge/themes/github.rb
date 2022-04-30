# -*- coding: utf-8 -*- #
# frozen_string_literal: true

module Rouge
  module Themes
    class Github < CSSTheme
      name 'github'

      style Comment::Multiline,               :fg => '#999988', :italic => true
      style Comment::Preproc,                 :fg => '#999999', :bold => true
      style Comment::Single,                  :fg => '#999988', :italic => true
      style Comment::Special,                 :fg => '#999999', :italic => true, :bold => true
      style Comment,                          :fg => '#999988', :italic => true
      style Error,                            :fg => '#a61717', :bg => '#e3d2d2'
      style Generic::Deleted,                 :fg => '#000000', :bg => '#ffdddd'
      style Generic::Emph,                    :fg => '#000000', :italic => true
      style Generic::Error,                   :fg => '#aa0000'
      style Generic::Heading,                 :fg => '#999999'
      style Generic::Inserted,                :fg => '#000000', :bg => '#ddffdd'
      style Generic::Output,                  :fg => '#888888'
      style Generic::Prompt,                  :fg => '#555555'
      style Generic::Strong,                  :bold => true
      style Generic::Subheading,              :fg => '#aaaaaa'
      style Generic::Traceback,               :fg => '#aa0000'
      style Keyword::Constant,                :fg => '#000000', :bold => true
      style Keyword::Declaration,             :fg => '#000000', :bold => true
      style Keyword::Namespace,               :fg => '#000000', :bold => true
      style Keyword::Pseudo,                  :fg => '#000000', :bold => true
      style Keyword::Reserved,                :fg => '#000000', :bold => true
      style Keyword::Type,                    :fg => '#445588', :bold => true
      style Keyword,                          :fg => '#000000', :bold => true
      style Literal::Number::Float,           :fg => '#009999'
      style Literal::Number::Hex,             :fg => '#009999'
      style Literal::Number::Integer::Long,   :fg => '#009999'
      style Literal::Number::Integer,         :fg => '#009999'
      style Literal::Number::Oct,             :fg => '#009999'
      style Literal::Number,                  :fg => '#009999'
      style Literal::String::Affix,           :fg => '#000000', :bold => true
      style Literal::String::Backtick,        :fg => '#d14'
      style Literal::String::Char,            :fg => '#d14'
      style Literal::String::Doc,             :fg => '#d14'
      style Literal::String::Double,          :fg => '#d14'
      style Literal::String::Escape,          :fg => '#d14'
      style Literal::String::Heredoc,         :fg => '#d14'
      style Literal::String::Interpol,        :fg => '#d14'
      style Literal::String::Other,           :fg => '#d14'
      style Literal::String::Regex,           :fg => '#009926'
      style Literal::String::Single,          :fg => '#d14'
      style Literal::String::Symbol,          :fg => '#990073'
      style Literal::String,                  :fg => '#d14'
      style Name::Attribute,                  :fg => '#008080'
      style Name::Builtin::Pseudo,            :fg => '#999999'
      style Name::Builtin,                    :fg => '#0086B3'
      style Name::Class,                      :fg => '#445588', :bold => true
      style Name::Constant,                   :fg => '#008080'
      style Name::Decorator,                  :fg => '#3c5d5d', :bold => true
      style Name::Entity,                     :fg => '#800080'
      style Name::Exception,                  :fg => '#990000', :bold => true
      style Name::Function,                   :fg => '#990000', :bold => true
      style Name::Label,                      :fg => '#990000', :bold => true
      style Name::Namespace,                  :fg => '#555555'
      style Name::Tag,                        :fg => '#000080'
      style Name::Variable::Class,            :fg => '#008080'
      style Name::Variable::Global,           :fg => '#008080'
      style Name::Variable::Instance,         :fg => '#008080'
      style Name::Variable,                   :fg => '#008080'
      style Operator::Word,                   :fg => '#000000', :bold => true
      style Operator,                         :fg => '#000000', :bold => true
      style Text::Whitespace,                 :fg => '#bbbbbb'
      style Text,                             :bg => '#f8f8f8'
    end
  end
end
