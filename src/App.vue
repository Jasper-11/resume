<template>
  <div class="container">
    <header>
      <div class="header-content">
        <div class="profile-section">
          <div class="avatar">
            <div class="avatar-placeholder">
              <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
              </svg>
            </div>
          </div>
          <div class="profile-info">
            <h1>{{ t('name') }}</h1>
            <p class="subtitle">{{ t('title') }}</p>
            <div class="contact">
              <span>{{ t('languages') }}</span> |
              <span>{{ t('citizenship') }}</span> |
              <span>{{ t('visa') }}</span>
              <br />
              <span>Email: <a :href="`mailto:${t('email')}`">{{ t('email') }}</a></span> |
              <span>{{ t('phone1') }}</span> |
              <span>{{ t('phone2') }}</span>
            </div>
          </div>
        </div>
        <div class="lang-toggle-container">
          <button class="lang-toggle" @click="toggleLang">
            <span class="current-lang">
              <span v-if="lang === 'en'">🇬🇧 English</span>
              <span v-else>🇻🇳 Tiếng Việt</span>
            </span>
            <span class="toggle-arrow">▼</span>
          </button>
          <div class="lang-dropdown">
            <div class="lang-option" :class="{ active: lang === 'en' }" @click="lang = 'en'">
              🇬🇧 English
            </div>
            <div class="lang-option" :class="{ active: lang === 'vi' }" @click="lang = 'vi'">
              🇻🇳 Tiếng Việt
            </div>
          </div>
        </div>
      </div>
    </header>

    <main>
      <div class="tabs">
        <button 
          v-for="tab in tabs" 
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="['tab-button', { active: activeTab === tab.id }]"
        >
          <span class="tab-icon">{{ tab.icon }}</span>
          {{ t(tab.name) }}
        </button>
      </div>

      <div class="tab-content">
        <!-- Summary Tab -->
        <div v-if="activeTab === 'summary'" class="tab-panel">
          <div class="section-header">
            <div class="section-icon">📋</div>
            <h2>{{ t('summaryTitle') }}</h2>
          </div>
          <div class="experience-grid">
            <div v-for="(experience, index) in t('summaryExperiences')" :key="index" class="experience-card">
              <div class="card-icon">{{ experience.icon }}</div>
              <h3>{{ experience.title }}</h3>
              <p>{{ experience.description }}</p>
            </div>
          </div>
        </div>

        <!-- Work Experience Tab -->
        <div v-if="activeTab === 'experience'" class="tab-panel">
          <div class="section-header">
            <div class="section-icon">💼</div>
            <h2>{{ t('workTitle') }}</h2>
          </div>
          <div class="timeline">
            <div v-for="(job, idx) in t('jobs')" :key="idx" class="job">
              <div class="job-header">
                <div class="company-logo">{{ job.icon }}</div>
                <div class="job-info">
                  <h3>{{ job.company }}</h3>
                  <p class="job-title">{{ job.title }}</p>
                  <p class="job-period">{{ job.period }}</p>
                  <p class="job-location" v-if="job.location">{{ job.location }}</p>
                </div>
              </div>
              <div class="job-achievements">
                <template v-for="(section, sidx) in job.sections" :key="sidx">
                  <h4>{{ section.heading }}</h4>
                  <ul>
                    <li v-for="(item, iidx) in section.items" :key="iidx">{{ item }}</li>
                  </ul>
                </template>
              </div>
            </div>
          </div>
        </div>

        <!-- Skills Tab -->
        <div v-if="activeTab === 'skills'" class="tab-panel">
          <div class="section-header">
            <div class="section-icon">🛠️</div>
            <h2>{{ t('skillsTitle') }}</h2>
          </div>
          <div class="skills-grid">
            <div v-for="(cat, idx) in t('skills')" :key="idx" class="skill-category">
              <h3>{{ cat.category }}</h3>
              <div class="skill-tags">
                <span v-for="(skill, sidx) in cat.items" :key="sidx" class="skill-tag">{{ skill }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Education Tab -->
        <div v-if="activeTab === 'education'" class="tab-panel">
          <div class="section-header">
            <div class="section-icon">🎓</div>
            <h2>{{ t('educationTitle') }}</h2>
          </div>
          <div class="education-section">
            <div class="education-card">
              <div class="education-icon">🏫</div>
              <div class="education-info">
                <h3>{{ t('education.school') }}</h3>
                <p class="degree">{{ t('education.degree') }}</p>
                <p class="graduation">{{ t('education.graduation') }}</p>
                <p class="location">{{ t('education.location') }}</p>
              </div>
            </div>
          </div>

          <div class="certifications-section">
            <h3>{{ t('certificationsTitle') }}</h3>
            <div class="certifications-grid">
              <div v-for="(cert, idx) in t('certifications')" :key="idx" class="certification-card">
                <span class="cert-icon">{{ cert.icon }}</span>
                <span>{{ cert.name }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Contact Tab -->
        <div v-if="activeTab === 'contact'" class="tab-panel">
          <div class="section-header">
            <div class="section-icon">📞</div>
            <h2>{{ t('contactTitle') }}</h2>
          </div>
          <div class="contact-section">
            <div class="contact-info">
              <h3>{{ t('contactInfoTitle') }}</h3>
              <div class="contact-grid">
                <div class="contact-item">
                  <span class="contact-icon">📧</span>
                  <span>Email: <a :href="`mailto:${t('email')}`">{{ t('email') }}</a></span>
                </div>
                <div class="contact-item">
                  <span class="contact-icon">📱</span>
                  <span>{{ t('phone1') }}</span>
                </div>
                <div class="contact-item">
                  <span class="contact-icon">📱</span>
                  <span>{{ t('phone2') }}</span>
                </div>
              </div>
            </div>

            <div class="references-section">
              <h3>{{ t('referencesTitle') }}</h3>
              <div class="references-grid">
                <div v-for="(ref, idx) in t('references')" :key="idx" class="reference-card">
                  <div class="reference-header">
                    <span class="reference-icon">{{ ref.icon }}</span>
                    <div>
                      <h4>{{ ref.name }}</h4>
                      <p>{{ ref.role }}</p>
                    </div>
                  </div>
                  <div class="reference-contact">
                    <p><a :href="`mailto:${ref.email}`">{{ ref.email }}</a></p>
                    <p>{{ ref.phone }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const lang = ref('en')
const toggleLang = () => {
  lang.value = lang.value === 'en' ? 'vi' : 'en'
}

const activeTab = ref('summary')

const tabs = [
  { id: 'summary', name: 'tabSummary', icon: '📋' },
  { id: 'experience', name: 'tabExperience', icon: '💼' },
  { id: 'skills', name: 'tabSkills', icon: '🛠️' },
  { id: 'education', name: 'tabEducation', icon: '🎓' },
  { id: 'contact', name: 'tabContact', icon: '📞' }
]

const data = {
  en: {
    name: 'Jasper E. Karlen',
    title: 'Systems Engineer & IT Professional',
    languages: 'English (native), French (limited)',
    citizenship: 'Australian & Canadian',
    visa: 'NAFTA Professional (USA/Mexico), UK Tier 5 eligible',
    email: 'Jasper.E.Karlen@gmail.com',
    phone1: '+1 778 697 7404',
    phone2: '+52 56 1062 6734',
    tabSummary: 'Summary',
    tabExperience: 'Experience',
    tabSkills: 'Skills',
    tabEducation: 'Education',
    tabContact: 'Contact',
    summaryTitle: 'Summary & Key Experiences',
    summaryExperiences: [
      { icon: '👥', title: 'Team Leadership', description: 'Experience starting a team from the ground up and developing it to be efficient and well respected within the company.' },
      { icon: '🎓', title: 'Training & Onboarding', description: 'Experience with onboarding and training of staff, both on and offshore.' },
      { icon: '🔄', title: 'Agile Methodology', description: '2 years of experience driving the adoption of the Agile methodology across 2 teams as a part time Iteration Manager, part time Systems Engineer.' },
      { icon: '🤖', title: 'Automation & Monitoring', description: 'Designed, developed and implemented numerous automation and monitoring initiatives on business critical infrastructure & applications (e.g. SWIFT, Control-M, SCOM).' },
      { icon: '⚙️', title: 'Systems Engineering', description: '10+ years of experience as a professional Systems Engineer/Administrator working in 24x7 IT operational environments within the financial industry.' },
      { icon: '📊', title: 'Best Practices', description: 'Developed product usage best practices and implemented them company wide, including improved batch scheduling standards and monitoring usage.' },
      { icon: '📈', title: 'Management Reporting', description: 'Built numerous reports for upper management regarding the health of specific applications and team performance.' },
      { icon: '🌍', title: 'Diverse Workplace', description: 'Experience working collaboratively in a highly diverse workplace with over 65 different nationalities.' },
      { icon: '🚨', title: 'Critical Incident Management', description: 'Experience as a Critical Incident Manager and point of escalation for a roughly $800 billion company.' }
    ],
    workTitle: 'Work Experience',
    jobs: [
      {
        icon: '🖥️',
        company: 'Global Relay',
        title: 'Operations – Linux Systems Administrator',
        period: 'June 2020 to Current',
        location: 'Vancouver, BC, Canada',
        sections: [
          { heading: 'Automation:', items: [
            'Reworked teams set of PowerShell scripts used for handling Onboarding & Off-boarding as well as various other administrative tasks',
            'Held regular PowerShell training sessions to upskill members of my team',
            'Worked on initiatives in Ansible AWX to automate various manual activities',
            'Developed a Django based dashboard to aid with tracking critical server patch status',
            'Developed and managed Puppet modules for maintaining server configuration'
          ]},
          { heading: 'Server Administration:', items: [
            'Patched production physical and virtual machines',
            'Investigated & resolved various OS & Hardware failures',
            'Provisioned new Physical & Virtual Centos & Rocky machines'
          ]}
        ]
      },
      {
        icon: '🏛️',
        company: 'Abu Dhabi Investment Authority (ADIA)',
        title: 'Technology Operations (TechOps) – Senior Associate',
        period: 'Mar 2015 to Apr 2019',
        location: 'Abu Dhabi, UAE',
        sections: [
          { heading: 'Automation & Monitoring:', items: [
            'Automated daily stop/start and critical event monitoring for SWIFT Alliance Access',
            'Automated collection of statistics and alerting for critical Tibco message queues',
            'Automated reporting and tracking of Control-M job counts and repeat failures with an aim to maintain a 99.8% success rate across 1500 job executions daily',
            'Wrote and implemented scripts for automated GIT deployments',
            'Automated critical financial market data checks',
            'Designed and implemented automated synthetic transactions for monitoring & alerting purposes'
          ]},
          { heading: 'Standards Development:', items: [
            'Instrumental in moving the team towards a documentation based approach',
            'Ran numerous Application Working Groups where we would discuss in-depth, the state of an application, any recent errors and continuous improvement initiatives'
          ]},
          { heading: 'Incident Management:', items: [
            'Performed key roles in disaster recovery simulations across two DR sites',
            'Managed simultaneous incidents effectively'
          ]},
          { heading: 'Subject Matter Expert:', items: [
            'Responsible for the on boarding and training of numerous new hires',
            'Engaged in all activities within the team. "Go-to" source for information for many colleagues across the department',
            'Mentored/guided multiple university students and graduates as part of the company\'s graduate program',
            'Leveraged my expert knowledge in Control-M to implement multiple new functionalities in a pre-existing environment, notably the use of "maybe conditions" and Time Zone scheduling functionality'
          ]}
        ]
      },
      {
        icon: '🏦',
        company: 'Suncorp Group LTD',
        title: 'Operations Support & Application Health – Systems Engineer',
        period: 'July 2011 to February 2015',
        location: 'Brisbane, QLD, Australia',
        sections: [
          { heading: 'Platform Owner:', items: [
            'Platform Owner for SCOM and 2IC for FireScope',
            'Upgraded our SCOM 2007 environment to a highly available SCOM 2012 configuration',
            'Fine-tuned SCOM monitoring to increase exchange health visibility and reduce noise'
          ]},
          { heading: 'Standardisation & Partnering:', items: [
            'Standardised and comprehensively documented many of our team\'s services in preparation for shifting the work overseas',
            'Travelled to China (1 month) to meet our offshore partners and up skill them in the delivery of these services',
            'Continued to standardise all of our services and their FireScope structural configuration'
          ]},
          { heading: 'Iteration Manager (for two teams):', items: [
            'Converted the teams into a new way of working by making them agile in their delivery',
            'Managed the teams\' workload and removed \'blockers\'',
            'Planned incoming work; ensured focus on highest value work items',
            'Tracked and reported on progress of the teams'
          ]},
          { heading: 'Batch Scheduling:', items: [
            'Responsible for Batch Scheduling and administration of Control-M in an environment with 20,000+ daily job executions across linux, windows and z/OS'
          ]}
        ]
      }
    ],
    skillsTitle: 'Technical Skills',
    skills: [
      { category: 'Enterprise Tools', items: ['Vsphere', 'RedHat (IDM & Satellite)', 'Exchange', 'Control-M Enterprise Manager', 'SWIFT', 'Informatica', 'Tibco', 'Flextrade', 'Remedy', 'Confluence', 'Jira', 'GIT', 'Active Directory', 'Microsoft IIS', 'Microsoft Office', 'RightAnswers', 'ServiceNow'] },
      { category: 'Monitoring Tools', items: ['Zabbix', 'Firescope', 'Tosca', 'BMC ProactiveNet', 'BMC TrueSight', 'BMC Portal/Patrol', 'Splunk', 'Kibana', 'Grafana', 'System Center Operations Manager (SCOM)', 'Tivoli'] },
      { category: 'Languages/Technologies', items: ['Python', 'Powershell', 'Ansible', 'Puppet', 'Django', 'Docker', 'Javascript', 'Node.js', 'Angular', 'PostgreSql', 'MongoDB', 'SQL', 'Perl', 'Bash', 'Shell', 'SFTP/FTP', 'SNMP', 'SOAP', 'REST', 'XML'] },
      { category: 'Operating Systems', items: ['RHEL6+', 'CentOS', 'Windows Server 2k19 to 2k3'] }
    ],
    educationTitle: 'Education & Qualifications',
    education: {
      school: 'Queensland University of Technology',
      degree: 'Bachelor of Information Technology',
      graduation: 'Graduated with Distinction (2008–2011)',
      location: 'Brisbane, QLD, Australia'
    },
    certificationsTitle: 'Certifications & Training',
    certifications: [
      { icon: '🧪', name: 'Tosca - Tricentis Certified Professional' },
      { icon: '💳', name: 'SWIFT - Operating Alliance Access and Entry' },
      { icon: '⚡', name: 'Powershell – Scripting Training Course' },
      { icon: '📋', name: 'ITIL Foundation Certificate in IT Service Management' },
      { icon: '⚙️', name: 'Control-M – Advanced Operation & Administration' },
      { icon: '🌐', name: 'Cisco Certified Network Associate 1&2' },
      { icon: '📊', name: 'SCOM – Administration Course' }
    ],
    contactTitle: 'Contact & References',
    contactInfoTitle: 'Contact Information',
    referencesTitle: 'Professional References',
    references: [
      { icon: '👨‍💼', name: 'James Davidson', role: 'Former Manager', email: 'James.Davidson@adia.ae', phone: '+971 50 409 3017 (GMT+4)' },
      { icon: '👨‍💻', name: 'James Templeton', role: 'Former Snr. Colleague', email: 'James.Templeton@adia.ae', phone: '+971 50 409 3071 (GMT+4)' },
      { icon: '👨‍🔧', name: 'Adam Hackett', role: 'Former Team Lead', email: 'Adam.Hackett@suncorp.com.au', phone: '+61 411 093 650 (GMT+10)' }
    ]
  },
  vi: {
    name: 'Jasper E. Karlen',
    title: 'Kỹ Sư Hệ Thống & Chuyên Gia CNTT',
    languages: 'Tiếng Anh (bản ngữ), Tiếng Pháp (cơ bản)',
    citizenship: 'Quốc tịch Úc & Canada',
    visa: 'Chuyên gia NAFTA (Mỹ/Mexico), đủ điều kiện UK Tier 5',
    email: 'Jasper.E.Karlen@gmail.com',
    phone1: '+1 778 697 7404',
    phone2: '+52 56 1062 6734',
    tabSummary: 'Tóm tắt',
    tabExperience: 'Kinh nghiệm',
    tabSkills: 'Kỹ năng',
    tabEducation: 'Học vấn',
    tabContact: 'Liên hệ',
    summaryTitle: 'Tóm tắt & Kinh nghiệm chính',
    summaryExperiences: [
      { icon: '👥', title: 'Lãnh đạo nhóm', description: 'Kinh nghiệm xây dựng và phát triển đội ngũ từ đầu, nâng cao hiệu quả và uy tín trong tổ chức.' },
      { icon: '🎓', title: 'Đào tạo & Hội nhập', description: 'Kinh nghiệm đào tạo và hội nhập nhân viên mới, cả trong và ngoài nước.' },
      { icon: '🔄', title: 'Phương pháp Agile', description: '2 năm thúc đẩy áp dụng phương pháp Agile cho 2 nhóm với vai trò Quản lý Vòng lặp và Kỹ sư Hệ thống.' },
      { icon: '🤖', title: 'Tự động hóa & Giám sát', description: 'Thiết kế, phát triển và triển khai nhiều giải pháp tự động hóa và giám sát cho hạ tầng & ứng dụng trọng yếu (ví dụ: SWIFT, Control-M, SCOM).' },
      { icon: '⚙️', title: 'Kỹ sư hệ thống', description: 'Hơn 10 năm làm việc chuyên nghiệp trong môi trường CNTT 24/7 tại các tổ chức tài chính.' },
      { icon: '📊', title: 'Thực tiễn tốt nhất', description: 'Xây dựng và triển khai các thực tiễn sử dụng sản phẩm, bao gồm chuẩn hóa lập lịch và giám sát.' },
      { icon: '📈', title: 'Báo cáo quản lý', description: 'Xây dựng nhiều báo cáo cho lãnh đạo về tình trạng ứng dụng và hiệu suất nhóm.' },
      { icon: '🌍', title: 'Môi trường đa dạng', description: 'Kinh nghiệm làm việc trong môi trường đa quốc gia với hơn 65 quốc tịch.' },
      { icon: '🚨', title: 'Quản lý sự cố nghiêm trọng', description: 'Đóng vai trò Quản lý Sự cố và điểm liên hệ cho công ty trị giá khoảng 800 tỷ USD.' }
    ],
    workTitle: 'Kinh nghiệm làm việc',
    jobs: [
      {
        icon: '🖥️',
        company: 'Global Relay',
        title: 'Quản trị viên Hệ thống Linux – Vận hành',
        period: '06/2020 – Nay',
        location: 'Vancouver, BC, Canada',
        sections: [
          { heading: 'Tự động hóa:', items: [
            'Cải tiến bộ script PowerShell cho quy trình hội nhập & rời công ty và các tác vụ quản trị khác',
            'Tổ chức đào tạo PowerShell thường xuyên cho thành viên nhóm',
            'Triển khai tự động hóa các tác vụ thủ công với Ansible AWX',
            'Phát triển dashboard Django theo dõi trạng thái cập nhật máy chủ',
            'Quản lý module Puppet cho cấu hình máy chủ'
          ]},
          { heading: 'Quản trị máy chủ:', items: [
            'Cập nhật bản vá cho máy chủ vật lý và ảo hóa',
            'Xử lý sự cố phần cứng & hệ điều hành',
            'Cấp phát máy chủ CentOS & Rocky mới'
          ]}
        ]
      },
      {
        icon: '🏛️',
        company: 'Abu Dhabi Investment Authority (ADIA)',
        title: 'Chuyên viên cao cấp – Vận hành Công nghệ (TechOps)',
        period: '03/2015 – 04/2019',
        location: 'Abu Dhabi, UAE',
        sections: [
          { heading: 'Tự động hóa & Giám sát:', items: [
            'Tự động hóa dừng/khởi động SWIFT Alliance Access và giám sát sự kiện quan trọng',
            'Thu thập thống kê và cảnh báo cho Tibco message queues',
            'Tự động báo cáo và theo dõi số lượng/lỗi Control-M (99.8% thành công trên 1500 job/ngày)',
            'Viết script triển khai GIT tự động',
            'Tự động kiểm tra dữ liệu thị trường tài chính',
            'Thiết kế giao dịch tổng hợp để giám sát & cảnh báo'
          ]},
          { heading: 'Phát triển tiêu chuẩn:', items: [
            'Thúc đẩy chuyển đổi nhóm sang mô hình tài liệu hóa',
            'Tổ chức các Nhóm Ứng dụng, thảo luận và cải tiến liên tục'
          ]},
          { heading: 'Quản lý sự cố:', items: [
            'Tham gia diễn tập phục hồi thảm họa tại 2 trung tâm',
            'Xử lý đồng thời nhiều sự cố nghiêm trọng'
          ]},
          { heading: 'Chuyên gia lĩnh vực:', items: [
            'Đào tạo và hội nhập nhiều nhân viên mới',
            'Là nguồn thông tin chính cho đồng nghiệp',
            'Hướng dẫn sinh viên và thực tập sinh',
            'Áp dụng chuyên môn Control-M để triển khai tính năng mới ("maybe conditions", lập lịch theo múi giờ)'
          ]}
        ]
      },
      {
        icon: '🏦',
        company: 'Suncorp Group LTD',
        title: 'Kỹ sư Hệ thống – Hỗ trợ vận hành & Sức khỏe ứng dụng',
        period: '07/2011 – 02/2015',
        location: 'Brisbane, QLD, Australia',
        sections: [
          { heading: 'Chủ sở hữu nền tảng:', items: [
            'Chủ sở hữu SCOM, phó quản trị FireScope',
            'Nâng cấp SCOM 2007 lên cấu hình HA 2012',
            'Tối ưu giám sát SCOM, giảm cảnh báo nhiễu'
          ]},
          { heading: 'Chuẩn hóa & Hợp tác:', items: [
            'Chuẩn hóa, tài liệu hóa dịch vụ để chuyển giao cho đối tác nước ngoài',
            'Đào tạo đối tác tại Trung Quốc (1 tháng)',
            'Tiếp tục chuẩn hóa cấu trúc FireScope'
          ]},
          { heading: 'Quản lý vòng lặp:', items: [
            'Chuyển đổi nhóm sang phương pháp Agile',
            'Quản lý khối lượng công việc, loại bỏ trở ngại',
            'Lập kế hoạch, ưu tiên công việc giá trị cao',
            'Theo dõi và báo cáo tiến độ'
          ]},
          { heading: 'Lập lịch batch:', items: [
            'Quản trị Control-M với hơn 20.000 job/ngày trên Linux, Windows, z/OS'
          ]}
        ]
      }
    ],
    skillsTitle: 'Kỹ năng chuyên môn',
    skills: [
      { category: 'Công cụ doanh nghiệp', items: ['Vsphere', 'RedHat (IDM & Satellite)', 'Exchange', 'Control-M Enterprise Manager', 'SWIFT', 'Informatica', 'Tibco', 'Flextrade', 'Remedy', 'Confluence', 'Jira', 'GIT', 'Active Directory', 'Microsoft IIS', 'Microsoft Office', 'RightAnswers', 'ServiceNow'] },
      { category: 'Công cụ giám sát', items: ['Zabbix', 'Firescope', 'Tosca', 'BMC ProactiveNet', 'BMC TrueSight', 'BMC Portal/Patrol', 'Splunk', 'Kibana', 'Grafana', 'System Center Operations Manager (SCOM)', 'Tivoli'] },
      { category: 'Ngôn ngữ/Công nghệ', items: ['Python', 'Powershell', 'Ansible', 'Puppet', 'Django', 'Docker', 'Javascript', 'Node.js', 'Angular', 'PostgreSql', 'MongoDB', 'SQL', 'Perl', 'Bash', 'Shell', 'SFTP/FTP', 'SNMP', 'SOAP', 'REST', 'XML'] },
      { category: 'Hệ điều hành', items: ['RHEL6+', 'CentOS', 'Windows Server 2k19 đến 2k3'] }
    ],
    educationTitle: 'Học vấn & Bằng cấp',
    education: {
      school: 'Đại học Công nghệ Queensland',
      degree: 'Cử nhân Công nghệ Thông tin',
      graduation: 'Tốt nghiệp loại Giỏi (2008–2011)',
      location: 'Brisbane, QLD, Australia'
    },
    certificationsTitle: 'Chứng chỉ & Đào tạo',
    certifications: [
      { icon: '🧪', name: 'Tosca - Chuyên gia được chứng nhận Tricentis' },
      { icon: '💳', name: 'SWIFT - Vận hành Alliance Access và Entry' },
      { icon: '⚡', name: 'Powershell – Khóa đào tạo lập trình nâng cao' },
      { icon: '📋', name: 'Chứng chỉ ITIL Foundation về Quản lý Dịch vụ CNTT' },
      { icon: '⚙️', name: 'Control-M – Vận hành & Quản trị nâng cao' },
      { icon: '🌐', name: 'Chứng chỉ Cisco Certified Network Associate 1&2' },
      { icon: '📊', name: 'SCOM – Khóa quản trị hệ thống' }
    ],
    contactTitle: 'Liên hệ & Tham chiếu',
    contactInfoTitle: 'Thông tin liên hệ',
    referencesTitle: 'Người tham chiếu chuyên môn',
    references: [
      { icon: '👨‍💼', name: 'James Davidson', role: 'Quản lý cũ', email: 'James.Davidson@adia.ae', phone: '+971 50 409 3017 (GMT+4)' },
      { icon: '👨‍💻', name: 'James Templeton', role: 'Đồng nghiệp cao cấp', email: 'James.Templeton@adia.ae', phone: '+971 50 409 3071 (GMT+4)' },
      { icon: '👨‍🔧', name: 'Adam Hackett', role: 'Trưởng nhóm cũ', email: 'Adam.Hackett@suncorp.com.au', phone: '+61 411 093 650 (GMT+10)' }
    ]
  }
}

const t = (key) => {
  const d = data[lang.value]
  if (!d) return ''
  if (typeof d[key] !== 'undefined') return d[key]
  // Support nested keys
  const keys = key.split('.')
  let val = d
  for (const k of keys) {
    if (val && typeof val === 'object' && k in val) {
      val = val[k]
    } else {
      return ''
    }
  }
  return val
}
</script>

<style>
body {
  margin: 0;
  font-family: 'Segoe UI', Arial, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #f3f3f3;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  background: rgba(35, 39, 43, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  margin-top: 2rem;
  margin-bottom: 2rem;
  overflow: hidden;
}

header {
  background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
  padding: 2rem;
  position: relative;
  overflow: hidden;
}

header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="75" cy="75" r="1" fill="rgba(255,255,255,0.1)"/><circle cx="50" cy="10" r="0.5" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
  opacity: 0.3;
}

.header-content {
  position: relative;
  z-index: 1;
}

.profile-section {
  display: flex;
  align-items: center;
  gap: 2rem;
  text-align: left;
}

.avatar {
  flex-shrink: 0;
}

.avatar-placeholder {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2rem;
  box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}

.avatar-placeholder svg {
  width: 40px;
  height: 40px;
}

.profile-info h1 {
  margin: 0;
  font-size: 2.5rem;
  color: #fff;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.subtitle {
  color: #8ab4f8;
  font-size: 1.2rem;
  margin: 0.5rem 0;
}

.contact {
  color: #b0b8c1;
  font-size: 0.9rem;
  margin-top: 1rem;
  line-height: 1.6;
}

.tabs {
  display: flex;
  background: rgba(52, 58, 64, 0.8);
  border-bottom: 1px solid rgba(255,255,255,0.1);
  overflow-x: auto;
}

.tab-button {
  background: none;
  border: none;
  color: #b0b8c1;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
  position: relative;
}

.tab-button:hover {
  color: #8ab4f8;
  background: rgba(138, 180, 248, 0.1);
}

.tab-button.active {
  color: #8ab4f8;
  background: rgba(138, 180, 248, 0.2);
  border-bottom: 3px solid #8ab4f8;
}

.tab-icon {
  font-size: 1.2rem;
}

.tab-content {
  padding: 2rem;
}

.tab-panel {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.section-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid rgba(138, 180, 248, 0.3);
}

.section-icon {
  font-size: 2rem;
}

.section-header h2 {
  color: #8ab4f8;
  margin: 0;
  font-size: 1.8rem;
}

/* Summary Tab Styles */
.experience-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.experience-card {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 12px;
  padding: 1.5rem;
  border-left: 4px solid #8ab4f8;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.experience-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

.card-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.experience-card h3 {
  color: #8ab4f8;
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
}

.experience-card p {
  color: #b0b8c1;
  line-height: 1.6;
  margin: 0;
}

/* Work Experience Tab Styles */
.timeline {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.job {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 12px;
  padding: 2rem;
  border-left: 4px solid #8ab4f8;
  position: relative;
}

.job::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 2rem;
  width: 16px;
  height: 16px;
  background: #8ab4f8;
  border-radius: 50%;
  box-shadow: 0 0 0 4px rgba(138, 180, 248, 0.2);
}

.job-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.company-logo {
  font-size: 2.5rem;
  background: rgba(138, 180, 248, 0.2);
  border-radius: 12px;
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.job-info h3 {
  color: #8ab4f8;
  margin: 0 0 0.25rem 0;
  font-size: 1.3rem;
}

.job-title {
  color: #f3f3f3;
  margin: 0 0 0.25rem 0;
  font-weight: 500;
}

.job-period {
  color: #b0b8c1;
  margin: 0 0 0.25rem 0;
  font-size: 0.9rem;
}

.job-location {
  color: #8ab4f8;
  margin: 0;
  font-size: 0.9rem;
  font-style: italic;
}

.job-achievements h4 {
  color: #8ab4f8;
  margin: 1.5rem 0 0.5rem 0;
  font-size: 1.1rem;
}

.job-achievements h4:first-of-type {
  margin-top: 0;
}

.job-achievements ul {
  margin: 0 0 1rem 0;
  padding-left: 1.5rem;
}

.job-achievements li {
  color: #b0b8c1;
  margin-bottom: 0.5rem;
  line-height: 1.6;
}

/* Skills Tab Styles */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.skill-category {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 12px;
  padding: 1.5rem;
}

.skill-category h3 {
  color: #8ab4f8;
  margin: 0 0 1rem 0;
  font-size: 1.2rem;
}

.skill-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.skill-tag {
  background: rgba(138, 180, 248, 0.2);
  color: #8ab4f8;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  border: 1px solid rgba(138, 180, 248, 0.3);
  transition: all 0.3s ease;
}

.skill-tag:hover {
  background: rgba(138, 180, 248, 0.3);
  transform: translateY(-1px);
}

/* Education Tab Styles */
.education-section {
  margin-bottom: 2rem;
}

.education-card {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 12px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.education-icon {
  font-size: 3rem;
  background: rgba(138, 180, 248, 0.2);
  border-radius: 12px;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.education-info h3 {
  color: #8ab4f8;
  margin: 0 0 0.5rem 0;
  font-size: 1.4rem;
}

.degree {
  color: #f3f3f3;
  margin: 0 0 0.25rem 0;
  font-weight: 500;
}

.graduation {
  color: #8ab4f8;
  margin: 0 0 0.25rem 0;
  font-size: 0.9rem;
}

.location {
  color: #b0b8c1;
  margin: 0;
  font-size: 0.9rem;
}

.certifications-section h3 {
  color: #8ab4f8;
  margin: 2rem 0 1rem 0;
  font-size: 1.3rem;
}

.certifications-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.certification-card {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 8px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  transition: transform 0.3s ease;
}

.certification-card:hover {
  transform: translateY(-2px);
}

.cert-icon {
  font-size: 1.5rem;
}

.certification-card span:last-child {
  color: #b0b8c1;
  font-size: 0.9rem;
}

/* Contact Tab Styles */
.contact-section {
  display: grid;
  gap: 2rem;
}

.contact-info h3,
.references-section h3 {
  color: #8ab4f8;
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
}

.contact-grid {
  display: grid;
  gap: 1rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #b0b8c1;
}

.contact-icon {
  font-size: 1.2rem;
}

.references-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.reference-card {
  background: rgba(52, 58, 64, 0.6);
  border-radius: 12px;
  padding: 1.5rem;
  border-left: 4px solid #8ab4f8;
}

.reference-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.reference-icon {
  font-size: 2rem;
  background: rgba(138, 180, 248, 0.2);
  border-radius: 8px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.reference-header h4 {
  color: #8ab4f8;
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
}

.reference-header p {
  color: #b0b8c1;
  margin: 0;
  font-size: 0.9rem;
}

.reference-contact p {
  color: #b0b8c1;
  margin: 0.25rem 0;
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    margin: 1rem;
    border-radius: 12px;
  }
  
  .profile-section {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .tabs {
    flex-wrap: wrap;
  }
  
  .tab-button {
    flex: 1;
    min-width: 120px;
  }
  
  .experience-grid,
  .skills-grid,
  .certifications-grid,
  .references-grid {
    grid-template-columns: 1fr;
  }
  
  .job-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .education-card {
    flex-direction: column;
    text-align: center;
  }
  
  .lang-toggle-container {
    position: relative;
    top: auto;
    right: auto;
    margin: 1rem auto;
  }
  
  .lang-toggle {
    min-width: 120px;
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }
}

/* Scrollbar Styling */
::-webkit-scrollbar {
  width: 8px;
  background: #23272b;
}

::-webkit-scrollbar-thumb {
  background: #444950;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #5a6268;
}

/* Links */
a {
  color: #8ab4f8;
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: #a8c7fa;
  text-decoration: underline;
}

.lang-toggle-container {
  position: absolute;
  top: 2rem;
  right: 2rem;
  z-index: 10;
}

.lang-toggle {
  background: rgba(52, 58, 64, 0.8);
  color: #8ab4f8;
  border: 2px solid #8ab4f8;
  border-radius: 25px;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 140px;
  justify-content: center;
}

.lang-toggle:hover {
  background: #8ab4f8;
  color: #23272b;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(138, 180, 248, 0.3);
}

.current-lang {
  font-weight: 500;
}

.toggle-arrow {
  font-size: 0.8rem;
  transition: transform 0.3s ease;
}

.lang-toggle:hover .toggle-arrow {
  transform: rotate(180deg);
}

.lang-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: rgba(52, 58, 64, 0.95);
  border: 2px solid #8ab4f8;
  border-radius: 12px;
  margin-top: 0.5rem;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease;
}

.lang-toggle-container:hover .lang-dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.lang-option {
  padding: 0.75rem 1.5rem;
  cursor: pointer;
  transition: background 0.2s ease;
  color: #b0b8c1;
  border-bottom: 1px solid rgba(138, 180, 248, 0.2);
}

.lang-option:last-child {
  border-bottom: none;
}

.lang-option:hover {
  background: rgba(138, 180, 248, 0.1);
  color: #8ab4f8;
}

.lang-option.active {
  background: rgba(138, 180, 248, 0.2);
  color: #8ab4f8;
  font-weight: 500;
}
</style> 