#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ast
Version  : 2.1.0
Release  : 7
URL      : https://rubygems.org/downloads/ast-2.1.0.gem
Source0  : https://rubygems.org/downloads/ast-2.1.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bacon-colored_output
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-json_pure
BuildRequires : rubygem-kramdown
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rest-client
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-yard

%description
# AST
[![Build Status](https://travis-ci.org/whitequark/ast.png?branch=master)](https://travis-ci.org/whitequark/ast)
[![Code Climate](https://codeclimate.com/github/whitequark/ast.png)](https://codeclimate.com/github/whitequark/ast)
[![Coverage Status](https://coveralls.io/repos/whitequark/ast/badge.png?branch=master)](https://coveralls.io/r/whitequark/ast)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ast-2.1.0
gem spec %{SOURCE0} -l --ruby > rubygem-ast.gemspec

%build
gem build rubygem-ast.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ast-2.1.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/ast-2.1.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/LICENSE.MIT
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/README.YARD.md
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/ast.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/lib/ast.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/lib/ast/node.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/lib/ast/processor.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/lib/ast/processor/mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/lib/ast/sexp.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/ast-2.1.0/test/test_ast.rb
/usr/lib64/ruby/gems/2.3.0/specifications/ast-2.1.0.gemspec
