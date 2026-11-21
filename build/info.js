// ---------- info ----------
function iref(id, label) { const it = ITEMS.find(x => x.id === id); return `<button class="linkchip" data-goto="${id}" style="color:${CATS[it.cat].color}">${CATS[it.cat].emoji} ${esc(label || it.name)}</button>`; }
function byName(n) { const it = ITEMS.find(x => x.name === n); if (!it) throw new Error('No place called ' + n); return it.id; }
function refs(names) { return names.map(n => iref(byName(n))).join(' '); }
function renderSpecial() {
  const stops = [
    ['King Richard III Visitor Centre', 'Start where he was found: you can look down on the grave site.'],
    ['Richard III statue', 'The bronze king in the Cathedral gardens.'],
    ['Leicester Cathedral', 'His tomb of Swaledale stone, reburied here in 2015.'],
    ['Leicester Guildhall', 'The medieval guildhall next door.'],
    ['Castle Gardens & the Newarke', 'Walk down to the river past the remains of the castle.'],
    ['Bow Bridge', 'Where legend says his spur, and later his head, struck the bridge.'],
    ['Bosworth Battlefield Heritage Centre', 'Drive 30 minutes west to where he died in 1485.'],
  ];
  $('#specialTrail').innerHTML = '<ol>' + stops.map(([n, t]) => `<li style="margin-bottom:8px">${iref(byName(n))}<br>${esc(t)}</li>`).join('') + '</ol>';
}
function renderInfo() {
  const hq = { q: 'Clock Tower, Leicester', name: 'Haymarket Memorial Clock Tower', ta: true };
  $('#v-info').innerHTML = `
  <div class="hero"><img src="img/cover.svg" alt=""><div class="cap"><span style="color:#FFD23F;font-size:11px;font-weight:800;letter-spacing:2px">YOUR BASE</span><br><b>The Clock Tower</b><br><span style="font-size:13px">The Victorian clock tower at the centre of the city. Walking times in the guide are from here.</span></div></div>
  <div class="sec"><h2>🚗 Getting there</h2>
   <img src="img/transit.svg" alt="" style="width:100%;border-radius:12px;aspect-ratio:16/7;object-fit:cover">
   <div class="opt" style="border-color:#1E4D8C"><h4 style="background:#1E4D8C"><span>🚌 Park &amp; Ride</span><span>cheaper than city parking</span></h4><ol>
    <li>Leicester has Park &amp; Ride sites at <b>Birstall</b> (north, off the A6), <b>Enderby</b> (south-west, near M1 J21) and <b>Meynell's Gorse</b> (west), with buses into the centre, and parking is free for bus users. Check fares and times before you go.</li></ol></div>
   <div class="opt" style="border-color:#E0A526"><h4 style="background:#E0A526"><span>🅿️ Driving in</span><span>multi-storeys</span></h4><ol>
    <li>Central car parks include <b>Haymarket</b> (by the Clock Tower), <b>Highcross</b> and <b>St Margaret's</b>.</li></ol></div>
   <div class="opt" style="border-color:#1877D0"><h4 style="background:#1877D0"><span>🚆 By train</span><span>10–15 min walk</span></h4><ol>
    <li>Leicester station is on London Road. Walk down Granby Street to the Clock Tower, or along New Walk to the Museum.</li></ol></div>
   ${actions(hq, true)}
  </div>
  <div class="sec"><h2>🗓️ Two easy days</h2>
   <div class="day" style="background:#FDE3DF"><b>Day 1 · Romans, Richard &amp; the Lanes:</b> ${refs(['King Richard III Visitor Centre', 'Leicester Cathedral', 'Leicester Guildhall', 'Jewry Wall Museum', 'The Lanes & St Martin\'s', 'Mrs Bridges', 'The Wardrobe', 'Leicester Market', 'The Blue Boar', 'Kayal'])}</div>
   <div class="day" style="background:#DDEBFA"><b>Day 2 · Art, parks &amp; the Golden Mile:</b> ${refs(['New Walk', 'Leicester Museum & Art Gallery', 'LCB Depot', 'Phoenix', 'The Ale Wagon', 'The Golden Mile', 'Bobby\'s', 'Abbey Park', 'National Space Centre'])}</div>
  </div>
  <div class="sec"><h2>🛍️ Vintage &amp; records</h2>
   <div class="day" style="background:#FDEFD6"><b>Lanes and arcades crawl:</b> ${refs(['The Wardrobe', 'Above Ground', 'The Vintage Scene', 'Sue Ryder Vintage & Retro, Loseby Lane', 'Rockaboom', 'Henshin'])}</div>
  </div>
  <div class="sec"><h2>🎸 Nights out</h2>
   <div class="day" style="background:#EFE2F8"><b>Gigs, theatre &amp; games:</b> ${refs(['De Montfort Hall', 'O2 Academy Leicester', 'Curve', 'Phoenix', 'Escape Leicester', 'ReRoll Board Game Café'])}</div>
   <div class="day" style="background:#D8F3EE"><b>Old Town pub crawl:</b> ${refs(['The Blue Boar', 'The Two-Tailed Lion', 'The Salmon'])}</div>
  </div>
  <div class="sec"><h2>🚗 Day trips</h2>
   <div class="day" style="background:#D8F3EE"><b>Countryside &amp; canals:</b> ${refs(['Bradgate Park', 'Foxton Locks', 'Bosworth Battlefield Heritage Centre'])}</div>
   <div class="day" style="background:#FDEFD6"><b>Steam &amp; pies:</b> ${refs(['Great Central Railway', 'Melton Mowbray'])}</div>
  </div>
  <div class="sec"><h2>🏟️ Sport</h2>
   <div class="day" style="background:#DDEBFA">${refs(['King Power Stadium (Leicester City)', 'Welford Road (Leicester Tigers)'])}</div>
  </div>
  <div class="sec"><h2>🕐 Opening hours</h2><ul>
   <li>Leicester Market is busiest on Saturdays. Many small shops in the Lanes are closed or shorter-hours on Sundays.</li>
   <li>The Golden Mile restaurants open late. The street is packed around Diwali in late October or November.</li>
   <li>Book Curve shows and weekend dinners ahead.</li></ul></div>
  <div class="sec"><h2>⚠️ Before you go</h2><ul>
   <li>Independent places change often. Check each venue's own site or socials before a special trip, especially places marked "check".</li>
   <li>Map pins come from OpenStreetMap and are close but not exact; use the Directions buttons for door-to-door routes.</li>
   <li>Information was checked in November 2026. The illustrations are original artwork drawn for this guide.</li></ul>
   <button class="btn b-map" id="installAgain" style="width:100%;margin-top:8px">📲 Install this guide on your phone</button></div>
  <div class="sec"><h2>🔄 Updates</h2><p>The guide checks for new content whenever you're online. If something looks out of date, tap below to clear the saved copy and reload.</p>
  <button class="iconbtn" id="refreshBtn" style="padding:10px 14px;box-shadow:0 1px 5px rgba(0,0,0,.2)">Refresh guide</button></div>`;
}
