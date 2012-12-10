Name:		htmlparser
Summary:	Java library used to parse HTML
Version:	1.6
Release:	6
Source0:		htmlparser1_6_20060610.zip
Group:		Development/Java
License:	LGPLv2+
URL:		http://www.htmlparser.org/
BuildRequires:	java-rpmbuild java-devel jpackage-utils
BuildRequires:	xml-commons-apis junit ant
BuildArch:	noarch
%description
HTML Parser is a Java library used to parse HTML in either a linear or
nested fashion. Primarily used for transformation or extraction, it
features filters, visitors, custom tags and easy to use JavaBeans. It
is a fast, robust and well tested package.

%package javadoc
Summary:	Javadoc for %name
Group:		Development/Java
%description javadoc
Javadoc for %name.

%prep
%setup -q -n htmlparser1_6
%{__unzip} src.zip

%build
export CLASSPATH=`build-classpath sax2 junit`
%ant

%install
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -m644 lib/htmllexer.jar %{buildroot}%{_javadir}/htmllexer-%{version}.jar
%{__install} -m644 lib/htmlparser.jar %{buildroot}%{_javadir}/htmlparser-%{version}.jar
%create_jar_links

%{__mv} docs/javadoc javadoc
%{__mv} docs html

%{__mkdir_p} %{buildroot}%{_javadocdir}
cp -a javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%doc readme.txt license.txt html
%{_javadir}/htmllexer-%{version}.jar
%{_javadir}/htmllexer.jar
%{_javadir}/htmlparser-%{version}.jar
%{_javadir}/htmlparser.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-6mdv2011.0
+ Revision: 619486
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.6-5mdv2010.0
+ Revision: 437901
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.6-4mdv2009.1
+ Revision: 350287
- 2009.1 rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.6-3mdv2009.0
+ Revision: 247040
- rebuild

* Wed Mar 19 2008 Nicolas Vigier <nvigier@mandriva.com> 1.6-1mdv2008.1
+ Revision: 188882
- import htmlparser


