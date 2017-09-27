%global commit 32d0042a9993a8f83668df86b677a098d15a3cd0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner seandepagnier
%global project weather_routing_pi
%global plugin weather_routing

Name: opencpn-plugin-weather-routing
Summary: Weather routing plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
Weather routing plugin for OpenCPN

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
