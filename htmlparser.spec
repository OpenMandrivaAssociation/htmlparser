Name:		htmlparser
Summary:	Java library used to parse HTML
Version:	1.6
Release:	%mkrel 4
Source:		htmlparser1_6_20060610.zip
Group:		Development/Java
License:	LGPLv2+
URL:		http://www.htmlparser.org/
BuildRequires:	java-rpmbuild java-devel jpackage-utils
BuildRequires:	xml-commons-apis junit ant
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
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
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -m644 lib/htmllexer.jar %{buildroot}%{_javadir}/htmllexer-%{version}.jar
%{__install} -m644 lib/htmlparser.jar %{buildroot}%{_javadir}/htmlparser-%{version}.jar
%create_jar_links

%{__mv} docs/javadoc javadoc
%{__mv} docs html

%{__mkdir_p} %{buildroot}%{_javadocdir}
%{__cp} -a javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}

%clean
%{__rm} -Rf %{buildroot}

%files
%doc readme.txt license.txt html
%{_javadir}/htmllexer-%{version}.jar
%{_javadir}/htmllexer.jar
%{_javadir}/htmlparser-%{version}.jar
%{_javadir}/htmlparser.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
